$(document).ready(function(){
    var productForm = $(".form-product-ajax")
    productForm.submit(function(event){
        event.preventDefault();
        var thisForm = $(this)
        var actionEndPoint = thisForm.attr("action");
        //var actionEndPoint = thisForm.attr("data-endpoint")
        var httpMethod = thisForm.attr("method");
        var submitBtnAdd = thisForm.find(".cart_item_add");
        var submitBtnRemove = thisForm.find(".cart_item_remove");
        var formData = thisForm.serialize();
        
        if (typeof submitBtnAdd !== 'undefined' && typeof submitBtnAdd.prevObject[0][3] !== 'undefined'){
            var btnSerialzeAdd = submitBtnAdd.prevObject[0][3].name +"="+ submitBtnAdd.prevObject[0][3].value;
            formData = formData+"&"+btnSerialzeAdd;
        }else{
            var btnSerialzeAdd = submitBtnAdd.prevObject[0][2].name +"="+ submitBtnAdd.prevObject[0][2].value;
            formData = formData+"&"+btnSerialzeAdd;
        }
        
        if (typeof submitBtnRemove !== 'undefined' && typeof submitBtnRemove.prevObject[0][3] !== 'undefined'){
            var btnSerialzeRemove = submitBtnRemove.prevObject[0][3].name +"="+ submitBtnRemove.prevObject[0][3].value;
            formData = formData+"&"+btnSerialzeRemove;
        }else{
            var btnSerialzeRemove = submitBtnRemove.prevObject[0][2].name +"="+ submitBtnRemove.prevObject[0][2].value;
            formData = formData+"&"+btnSerialzeRemove;
        }

        $.ajax({
        url: actionEndPoint,
        method: httpMethod,
        data: formData,
        success: function(data){
            var submitSpan = thisForm.find(".submit-span")            
            if(data.added){
                submitSpan.html('<input type="hidden" id="cart_item_id" name="cart_item_id" value="'+data.cart_item_id+'"><div class="btn-group"><a class="btn btn-link" href="/cart/">In cart</a> <button type="submit" id="cart_item_remove" name="cart_item_remove" value="true" class="btn btn-danger">Remove</button></div>')
                console.log(data.cart_item_id)
            }else{
                submitSpan.html('<input id="product_quantity" name="product_quantity" type="number" min="1" max="'+data.productQty+'" value="1" /><button type="submit" id="cart_item_add" name="cart_item_add" value="true" class="btn btn-success btn-add">Add to cart</button>')
                console.log("data", data)
            }
            var navbarCount = $(".navbar-cart-count")
            navbarCount.text(data.cartItemCount)
            var currentPath = window.location.href
            if (currentPath.indexOf("cart") != -1){
            refreshCart()
            }
        },
        error: function(errorData){
            $.alert({
            title: "oops!",
            content: "an error occurred",
            theme: "modern",
            })
        }
        })
    })
})