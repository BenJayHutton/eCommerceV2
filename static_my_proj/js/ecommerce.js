$(document).ready(function(){
    var productForm = $(".form-product-ajax")
    productForm.submit(function(event){
      event.preventDefault();
      var thisForm = $(this)
      var actionEndPoint = thisForm.attr("action");
      //var actionEndPoint = thisForm.attr("data-endpoint")
      var httpMethod = thisForm.attr("method");
      var formData = thisForm.serialize();
      // console.log(formData)
      

  })
})

      
      
      // $.ajax({
      //   data: data,
      //   url: actionEndPoint,
      //   method: httpMethod,
      //   success: function(data){
      //     console.log(data)
      //   },
      //   error: function(error){
      //     console.log(error)
      //   }

      // })