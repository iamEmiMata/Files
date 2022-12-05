

//  Ventana modal Sencilla 

const open = document.getElementById('abrir');
const close = document.getElementById('cerrar');
const modal = document.getElementById('visible');

open.addEventListener('click', function () {
	modal.style.visibility = 'visible';
});


close.addEventListener('click', function() {
	modal.style.visibility = 'hidden';
});

window.addEventListener('click', function(event) {
	if (event.target == modal) {
		modal.style.visibility = 'visible';
	}
})