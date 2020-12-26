$(document).ready(function() {
    $('.button_cad_doenca').on('click', function(e) {
        e.preventDefault();
        var doenca = $('#nome').val();
        var sintomas = $('#sintomas').val();

        if(doenca != "" && sintomas != ""){
            $('#nome').val("");
            $('#sintomas').val("");
            $('#atencao').html('<span style="color: green;">Dados Cadastrados com Sucesso!</span>');
            $.ajax({
                method: "POST",
                url: '/processo_doenca',
                data: { doenca: doenca, sintomas: sintomas}
            });
        }else{
            $('#atencao').html('<span style="color: red;">É necessário preencher todos os campos!</span>');
        }

    });
    $('.button_cad').on('click', function(e) {
        e.preventDefault();
        var data_coleta = $('#data_coleta').val();
        var doenca_associada = $('#doenca_associada').val().toUpperCase();


        if(data_coleta != "" && doenca_associada != ""){
            $('#data_coleta').val("");
            $('#doenca_associada').val("");
            $('#atencao').html('<span style="color: green;">Dados Cadastrados com Sucesso!</span>');
            $.ajax({
                method: "POST",
                url: "/processo_epidemio",
                data: {data_coleta: data_coleta, doenca_associada: doenca_associada}
            });
        }else{
            $('#atencao').html('<span style="color: red;">É necessário preencher todos os campos!</span>');
        }
    });
});

var doencas = {};
$("select[name='doencas'] > option").each(function () {
    if(doencas[this.text]) {
        $(this).remove();
    } else {
        doencas[this.text] = this.value;
    }
});

var selectedSource;
function getSelected(){
selectedSource = $("#doencas").val();
    if (selectedSource != "SELCIONE UMA DOENÇA"){
        var context = document.getElementsByClassName("chart-line");
        var data_coleta = [];
        var recorrencia_na_data = [];               

        var tabela = document.getElementById("dataset");
        for(var i = 1; i < tabela.rows.length; i++){
            data_coleta.push(tabela.rows[i].cells[0].innerHTML);
        }
        var uniqueDatas = [];
        $.each(data_coleta, function(i, el){
            if($.inArray(el, uniqueDatas) === -1) uniqueDatas.push(el);
        });
        uniqueDatas.sort();

        var cont = 0;
        var table = document.getElementById("dataset");
        for(var k = 0; k < uniqueDatas.length; k++){
            for(var j = 1; j < table.rows.length; j++){
               if(uniqueDatas[k] === tabela.rows[j].cells[0].innerHTML){
                   if(selectedSource === tabela.rows[j].cells[1].innerHTML){
                       cont = cont + 1;
                   }
               }
            }
            recorrencia_na_data.push(cont);
        }

        var chartGraph = new Chart(context, {
            type: 'line',
            data: {
                labels: uniqueDatas,
                datasets: [{
                    label: selectedSource,
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: recorrencia_na_data,
                    borderWidth: 4,
                    backgroundColor: 'transparent',
                }]
            },
        });
    }
}


var hora = document.getElementById('mostrarHora');

function time() {
  var d = new Date();
  var s = d.getSeconds();
  var m = d.getMinutes();
  var h = d.getHours();

  if (h < 10){
      h = "0" + h
  }
  if (m < 10){
      m = "0" + m
  }
  if(s < 10){
      s = "0" + s
  }
  hora.textContent = "Hora Atual: " + h + ":" + m + ":" + s
  
}

setInterval(time, 1000);