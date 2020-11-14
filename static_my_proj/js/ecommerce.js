$(document).ready(function(){
    function getOwnedProduct(productId, submitSpan){
        var actionEndPoint = '/orders/endpoint/verify/ownership/';
        var httpMethod = 'GET';
        var data = {
            product_id: productId
        }
        var isOwner
        $.ajax({
            url: actionEndPoint,
            method: httpMethod,
            data: data,
            success: function(data){
                if (data.owner){
                    isOwner = true;
                    submitSpan.html("<a class='btn btn-warning' href='/library/'>In Library</a>");
                }else{
                    isOwner = false;
                }
            },
            error: function(error){
                console.log(error);
            }
        })
        return isOwner;
    }

    var formData = $(".form-product-ajax")
    $.each(formData, function(index, object){
        var $this = $(this);
        var isUser = $this.attr("data-user");
        var submitSpan = $this.find(".submit-span");
        var productInput = $this.find("[name='product_id']");
        var productId = productInput.attr("value");
        var productIsDigital = productInput.attr("data-is-digital");
        var isOwned;
        if (productIsDigital && isUser){
            var isOwned = getOwnedProduct(productId, submitSpan);
        }
    })
    
    formData.on('submit', function(event) {
        event.preventDefault();
        var thisForm = $(this)
        var cartSubmitBtn = event.originalEvent.submitter.attributes[3].value;
        var url = '/cart/update/'
        var method = 'POST'
        var data = thisForm.serialize();

        if(cartSubmitBtn == "cart_item_update"){
            data = data+"&"+cartSubmitBtn+"=true"
        }else if(cartSubmitBtn == "product_item_remove"){
            data = data+"&"+cartSubmitBtn+"=true"
        }else if(cartSubmitBtn == "cart_item_add"){
            data = data+"&"+cartSubmitBtn+"=true"
        }else if(cartSubmitBtn == "cart_item_remove"){
            data = data+"&"+cartSubmitBtn+"=true"
        }
        console.log("thisForm.serialised ", data)
        upDateOrder(url, method, data, thisForm)
    });

    function upDateOrder(url, method,formData, thisForm){
        $.ajax({
            url: url,
            method: method,
            data:formData,
            success: function(data){
                var submitSpan = thisForm.find(".submit-span")
                var cartItemRow = $("#"+data.cart_item_id)
                var cartItemPrice = $("#"+data.cart_item_id+" #cart_item_price")
                var contentBody = $(".content-body")
                console.log("cartItemRow", cartItemRow)
                if(data.updated){
                    var cartUpdateSpanTotal = $(".cart-total")
                    var cartUpdateSpanVatTotal = $(".cart-vattotal")
                    var cartUpdateSpanSubtotal = $(".cart-subtotal")
                    cartItemPrice.html(data.price_of_item);
                    cartUpdateSpanTotal.html(data.cart_total)
                    cartUpdateSpanVatTotal.html(data.cart_vat)
                    cartUpdateSpanSubtotal.html(data.cart_subtotal)
                }
                if(data.added){
                    submitSpan.html('<input type="hidden" id="cart_item_id" name="cart_item_id" value="'+data.cart_item_id+'"><div class="btn-group"><a class="btn btn-link" href="/cart/">In cart</a> <button onclick="this.form.submitted=this.value;" type="submit" id="product_item_remove" name="product_item_remove" value="true" class="btn btn-danger">Remove</button></div>')
                }
                if(data.removed){
                    submitSpan.html('<input id="product_quantity" name="product_quantity" type="number" min="1" max="'+data.productQty+'" value="1" /><button onclick="this.form.submitted=this.value;" type="submit" id="cart_item_add" name="cart_item_add" value="true" class="btn btn-success btn-add">Add to cart</button>')
                    cartItemRow.html("<td class='.text-muted'>Removed</td>")
                }

                if(data.cartItemCount < 1){
                    $(".cart-table").html("<p class='lead'>Cart is empty</p><a href='/products/' class='btn btn-success'><< Products</a>");
                }
                var navbarCount = $(".navbar-cart-count")
                navbarCount.text(data.cartItemCount);
                console.log("data", data);
            },
            error: function(error){
                console.log("error", error);
            }
        })
    }
})