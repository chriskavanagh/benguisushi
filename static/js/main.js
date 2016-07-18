$(function() {
	$("#logIcon").hover(function() {
		$('#formModal').modal();
		console.log("Success");
			
	}); // end hover
}); // end doc ready





/*
$(function() {
	$("#logIcon").mouseenter(function() {
		$('#formModal').modal();
			console.log('FadeIn');
		});
			$("#logIcon").mouseleave(function(){
				$('#formModal').modal().fadeOut('slow');
					console.log('FadeOut');
			});
				
			
	 // end hover
}); // end doc ready
*/




/*

$(function() {
	
	$("#logIcon").hover(function() {		
			$.ajax({
			type: 'GET',
			url: '/my-cart/',
			dataType: 'html',
			
			success: function(data) {
				console.log(data);
				//$('#popup').html(data);				
				$('.jumbotron').html(data);			
			   }
			
		}); // end ajax
	}); // end hover
}); // end document ready

*/

//use these in script to grab the data and place it in dialog box.
//var product = $('#id-for-product').val();  //from template item.product
//var price = $('#id-for-price').val();      //from template item.product.price

