
let tiempo = document.getElementById('time'),
    hora = document.getElementById('hour'),
    minutos = document.getElementById('min'),
    segundos = document.getElementById('seg');

showTime = () => {
    let d = new Date(),
        h = d.getHours(),
        m = d.getMinutes(),
        s = d.getSeconds();
    
    let ampm = h >= 12 ? 'PM' : 'AM';
    let Hora = h < 10 ? '0' + h : h;
    let Min = m < 10 ? '0' + m : m;
    let Segun2 = s < 10 ? '0' + s : s;

    hora.innerHTML = `${Hora}`;
    minutos.innerHTML = `${Min}`;
    segundos.innerHTML = `${Segun2}`;
    tiempo.innerHTML = `${ampm}`;
}

showTime();
let updateTime = setInterval(showTime, 1000);