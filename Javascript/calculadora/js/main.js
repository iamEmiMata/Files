uno = () => {
    document.screen.ans.value+='1';
}

dos = () => {
    document.screen.ans.value+='2';
}
tres = () => {
    document.screen.ans.value+='3';
}
cuatro = () => {
    document.screen.ans.value+='4';
}
cinco = () => {
    document.screen.ans.value+='5';
}
seis = () => {
    document.screen.ans.value+='6';
}
siete = () => {
    document.screen.ans.value+='7';
}
ocho = () => {
    document.screen.ans.value+='8';
}
nueve = () => {
    document.screen.ans.value+='9';
}
cero = () => {
    document.screen.ans.value+='0';
}

limpiar = () => {
    document.screen.ans.value='';
}

suma = () => {
    document.screen.ans.value+='+';
}

resta = () => {
    document.screen.ans.value+='-';
}

mult = () => {
    document.screen.ans.value+='*';
}

div = () => {
    document.screen.ans.value+='/';
}

resultado = () => {
    document.screen.ans.value=eval(document.screen.ans.value) + '' ;
}
