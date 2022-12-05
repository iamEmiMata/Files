let weekDays = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
let months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre','Octubre', 'Noviembre', 'Diciembre'];
let img = ['img1.jpg', 'img2.jpg','img3.jpg','img4.jpg', 'img5.jpg','img6.jpg','img7.jpg', 'img8.jpg','img9.jpg', 'img10.jpg', 'img11.jpg','img12.jpg'];


// Date
let d = new Date();
let currentDay = d.getDate();
let day = d.getDay();
let month = d.getMonth();
let year = d.getFullYear().toString();;
let h = d.getHours();
let min = d.getMinutes(2);

// buttons header
let last = document.getElementById('prev');
let next = document.getElementById('next');
//  Date header
let currentMonth = document.querySelector('.month');
let currentYear = document.querySelector('.year');
// week variables
let weekDaysGrid = document.getElementById('calendarDays');
let fullDaysGrid = document.getElementById('daysGrid');
// Current Date and hour 
let dw = document.getElementById('dayWeek');
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
    bgImg()
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
    bgImg()
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
        // console.log(weekDays[w][0]);
        if (weekDays[w] === weekDays[day-1]) {    
            dw.innerHTML += `<h4 class="date"><span id="dayWeek">${weekDays[w-1].slice(0, 3)},</span> <span>${currentDay} ${months[month].slice(0, 3)}, ${year.slice(-2)}</span></h4>`;
            bgImg()
        } else  {
            weekDaysGrid.innerHTML += `<div class="items"><span class='Day'>${weekDays[w].slice(0, 1)}</span></div>`;
        }

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
        fullDaysGrid.innerHTML += `<div class="items">
        <span class='before'> ${getTotalDays(month-1) - (start - 1)} </span>
        </div>`;    
    }

    // grid 
    console.log(month);
    for(let grid = 1; grid <= getTotalDays(month); grid++) {
        let x = grid < 10 ? '0' : '';
        if(grid == currentDay) { 
            fullDaysGrid.innerHTML += `<span class='Day currentDayG'>${x + grid}</span>`;
        } else {
            fullDaysGrid.innerHTML += `<span class='Day'>${x + grid}</span>`;
        }
    }
}

// img
function bgImg() {
    let upBox = document.getElementById("upImg");
    upBox.style.backgroundImage = `url(img/${img[month]})`;
}