let weekDays = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
let months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre'];

// Date
let d = new Date();
let currentDay = d.getDate();
let day = d.getDay();
let month = d.getMonth();
let year = d.getFullYear();
let h = d.getHours();
let min = d.getMinutes(2);


// buttons header
let last = document.getElementById('prev');
let next = document.getElementById('next');
//  Date header
let currentMonth = document.getElementById('month');
let currentYear = document.getElementById('year');
let diaSemana = document.getElementById('diaS');
// week variables
let weekDaysGrid = document.getElementById('calendarDays');
let fullDaysGrid = document.getElementById('daysGrid');

let fecha = document.getElementById('fecha');
fecha.innerHTML = `${currentDay}  ●  ${month}  ●  ${year}`;
let hour = document.getElementById('time');
showTime = () => {
    let d = new Date(),
        h = d.getHours(),
        m = d.getMinutes(),
        s = d.getSeconds();
    
    let ampm = h >= 12 ? 'PM' : 'AM';
    let Hora = h < 10 ? '0' + h : h;
    let Min = m < 10 ? '0' + m : m;
    let Segun2 = s < 10 ? '0' + s : s;

    hour.innerHTML = `${Hora} : ${Min} : ${Segun2} ${ampm}`;
}

showTime();
let updateTime = setInterval(showTime, 1000);
// header month and year output
currentMonth.textContent = months[month];
currentYear.textContent = year.toString();

// prev, last Button
last.addEventListener('click', ()=>lastMonth());
next.addEventListener('click', ()=>nextMonth());


writeTotalDays(month, currentDay); // Exit 

// Months Start Day
function startMonth() {
    let firstDay = new Date(year, month, 1);
    return((firstDay.getDay()-1) === -1) ? 6 : firstDay.getDay()-1;
}

//  button last
function lastMonth() {
    if(month !== 0) {
        month--;
    } else {
        month = 11;
        year--;
    }
    setNewDate();
}

//  button next
function nextMonth() {
    if(month !== 11) {
        month++;
    } else {
        month = 0;
        year++;
    }
    setNewDate();
}

//  Set date
function setNewDate() {
    d.setFullYear(year, month, currentDay);
    currentMonth.textContent = months[month];
    currentYear.textContent = year.toString();
    fullDaysGrid.textContent = '';
    writeTotalDays(month, currentDay);
}

// Week Letters
function weekLetters(day, weekDays) {
    for( let w = 0; w <= weekDays.length; w++) {
        if (weekDays[w] === weekDays[day-1]) {  
            diaSemana.textContent = weekDays[w-1] + ' 🌼';
        } 
        weekDaysGrid.innerHTML += `<div id="daysGrid" class="items"><span class='Day'>${weekDays[w].slice(0,1)}</span></div>`;
    }
}
weekLetters(day, weekDays); // Exit

// Lead Year ? True : False 
function lead(year) {
    if ((year % 100 !== 0) && (year % 4 === 0) || (year % 400 === 0)) {
        return 29;
    } else {
        return 28;
    }
}
lead(year); // Exit

function getTotalDays(month){
    if(month === -1) month = 11;

    if (month == 0 || month == 2 || month == 4 || month == 6 || month == 7 || month == 9 || month == 11) {
        console.log('31');
        return  31;

    } else if (month == 3 || month == 5 || month == 8 || month == 10) {
        console.log('30');
        return 30;

    } else {
        return lead(year);
    }
}
getTotalDays(month, currentDay); // Exit

function writeTotalDays(month, currentDay){
    // start Month 
    for(let start = startMonth(); start > 0; start--){
        fullDaysGrid.innerHTML += `<div id="daysGrid" class="items"><span class='Day'>
        <span class='before'> ${getTotalDays(month-1) - (start - 1)} </span></span>
        </div>`;    
    }

    // grid 
    console.log(month);
    for(let grid = 1; grid <= getTotalDays(month); grid++) {
        let x = grid < 10 ? '0' : '';

        if(grid == currentDay) { 
            fullDaysGrid.innerHTML += `<div id="daysGrid" class="items"><span class='Day currentDay'>${x + grid}</span></div>`;
        } else {
            fullDaysGrid.innerHTML += `<div id="daysGrid" class="items"><span class='Day'>${x + grid}</span></div>`;
        }
    }
}