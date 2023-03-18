let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');
let videoBtn = document.querySelectorAll('.vid-btn');

window.onscroll = () => {
	menu.classList.remove('fa-times');
	navbar.classList.remove('active');
}

menu.addEventListener('click', () => {
	menu.classList.toggle('fa-times');
	navbar.classList.toggle('active');
});

videoBtn.forEach(btn => {
	btn.addEventListener('click', () => {
		document.querySelector('.controls .active').classList.remove('active');
		btn.classList.add('active');
		let src = btn.getAttribute('data-src');
		document.querySelector('#video-slider').src = src;
	});
});

$(document).ready(()=>{

	$(document).on("submit", '#bookForm', (e)=> {
		e.preventDefault();
		var placename = $("#placename").val();
		var num_of_visitors = $("#num_of_visitors").val();
		var timeSlot = $("#timeSlot").val();
		let is_error = '';

		if(placename === "") {
			alert("Please enter place name");
			return;
		}

		if(num_of_visitors === "") {
			alert("Please enter number of visitors");
			return;
		}

		if(timeSlot === "") {
			alert("Please select your time slot");
			return;
		}


		if(is_error == '') {
			console.log(timeSlot);
			var formData = new FormData(document.getElementById("bookForm"));
			$.ajax({
				url: '/booking_confirmation/',
				type: 'post',
				data: formData,
				contentType:false,
				processData: false,
				beforeSend: function() {
					alert("Please wait...");
				},
				success: function (data) {
					if(data.status === 1){
						alert(data.message);
					}
				}
			})
		}
	})

	$(document).on("submit", '#emailForm', (e)=> {
		e.preventDefault();
		var name = $("#e-name").val();
		var email = $("#e-mail").val();
		var textarea = $("#e-textarea").val();
		let is_error = '';

		if(name === "") {
			alert("Please enter your name");
			return;
		}

		if(email === "") {
			alert("Please enter your email");
			return;
		}

		if(textarea === "") {
			alert("You can't leave the message empty");
			return;
		}


		if(is_error == '') {
			var formData = new FormData(document.getElementById("emailForm"));
			$.ajax({
				url: '/contact-us/',
				type: 'post',
				data: formData,
				contentType:false,
				processData: false,
				beforeSend: function() {
					alert("Please wait...");
				},
				success: function (data) {
					if(data.status === 1){
						alert(data.message);
					}
				}
			})
		}
	})
})