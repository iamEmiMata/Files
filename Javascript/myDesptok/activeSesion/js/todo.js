
let tarea = document.getElementById('tarea');
let addTarea = document.getElementById('addTarea');
let notifica = document.getElementById('msg');
let lista = document.getElementById('listaTarea');

//  add new 
addTarea.onclick = function() {
	if (tarea.value.length == 0) {
		notifica.innerHTML = '<section class="info"><span id="msg">⚠ Fill box to add new tasks!</span></section>';
	} else {
		lista.innerHTML += `
		<section class="valueTasks" id="listaTarea">
			<input type='checkbox' class='check'>
			<input type="text" rows='2' value="${tarea.value}" readonly>
			<button class='delete'>x</button>
		</section>
		`;
		notifica.innerHTML = '<section class="success"><span id="msg">Successfully Added!</span></section>';

		// delete
		let currentTask = document.querySelectorAll('.delete');
		for(let x = 0; x < currentTask.length; x++){
		    currentTask[x].onclick = function() {
		        this.parentNode.remove();
		        notifica.innerHTML = '<section class="damage"><span id="msg">Successfully Deleted!</span></section>';
		    }
		}

		// Ready msg
		let checked = document.querySelectorAll('.check');
		for(let x = 0; x < checked.length; x++){
		    checked[x].onclick = function() {
		        notifica.innerHTML = `<section class="info"><span id="msg">Tasks ${x+1} Successfully Completed!</span></section>`;
		    }
		}

	}

	limpiar();
}



let limpiar = () => {
    tarea.value = '';
};