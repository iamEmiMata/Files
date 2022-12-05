function changeColor(element) {
    var currentColor = element.style.backgroundColor;
    if(currentColor == 'white') {
        element.style.backgroundColor = '#70D6FF';
    } else {
        element.style.backgroundColor = 'white';
    }
}
function changeColor2(element) {
    var currentColor = element.style.backgroundColor;
    if(currentColor == 'white') {
        element.style.backgroundColor = '#FF70A6';
    } else {
        element.style.backgroundColor = 'white';
    }
}
function changeColor3(element) {
    var currentColor = element.style.backgroundColor;
    if(currentColor == 'white') {
        element.style.backgroundColor = '#FF9770';
    } else {
        element.style.backgroundColor = 'white';
    }
}
function changeColor4(element) {
    var currentColor = element.style.backgroundColor;
    if(currentColor == 'white') {
        element.style.backgroundColor = '#FFD670';
    } else {
        element.style.backgroundColor = 'white';
    }
}
function changeColor5(element) {
    var currentColor = element.style.backgroundColor;
    if(currentColor == 'white') {
        element.style.backgroundColor = '#E9FF70';
    } else {
        element.style.backgroundColor = 'white';
    }
}
function changeColor6(element) {
    var currentColor = element.style.backgroundColor;
    if(currentColor == 'white') {
        element.style.backgroundColor = '#B69DFC';
    } else {
        element.style.backgroundColor = 'white';
    }
}

function copyToClipboard(){
    let colorOutput = document.getElementById('idColor');
    colorOutput.select();
    document.execCommand('copy');
    alert('Palette Copied');
}