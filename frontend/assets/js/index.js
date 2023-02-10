// cuando todo el documento este cargado me ejecute la funcion inicial init
document.addEventListener("DOMContentLoaded", init);

// creamos una funcion para la url de nuestro servidor
const URL_API = "http://127.0.0.1:3000/";

let valoresTelemetria = [];

//funcion init
//va a cargar los datos  de nuestro sistema

function init() {
  verValoresTelemetria();
}

// ****************************************************
//creamos la funcion ver Datos
//creamos una funcion asyncrona

async function verValoresTelemetria() {
  // creamos una variable que agregamos la url principal y le agregamos la extension datos

  let url = URL_API + "InfoTelemetria";

  //hacer la peticion

  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-type": "application/json",
    },
  });

  valoresTelemetria = await response.json();

  console.log(valoresTelemetria);

  //crearemos el html
  //usaremos un ciclo para recorrer los usuarios

  let html = "";

  for (valor of valoresTelemetria) {
    let row = `

<tr>
 <td>${valor.id}</td>
 <td>${valor.nombreDispositivo}</td>
 <td>${valor.idmensaje}</td>
 <td>${valor.fechaDispositivo}</td>
 <td>${valor.latitud}</td>
 <td>${valor.longitud}</td>
 <td>${valor.temperatura}</td>
 <td>${valor.voltajeBateria}</td>
 <td>${valor.idevento}</td>
 <td>${valor.ciclando}</td>
 <td>${valor.vac}</td>
 <td>${valor.iac}</td>
 <td>${valor.vdc}</td>
 <td>${valor.idc}</td>
 <td>${valor.releciclado}</td>
 <td>${valor.releauxiliar}</td>
 <td>${valor.horometrovac}</td>
 <td>${valor.horometrovdc}</td>
 <td>${valor.fechagrabacion}</td>
 <td>${valor.descripcionevento}</td>
</tr>

`;
    html = html + row;
  }

  document.querySelector("#table-id > tbody").outerHTML = html;
}

//************************************************************** */

async function verValorTelemetria() {
  // creamos una variable que agregamos la url principal y le agregamos la extension datos

  let url = URL_API + "InfoTelemetria/" + "filtro";

  //hacer la peticion

  let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-type": "application/json",
    },
  });

  valoresTelemetria = await response.json();

  console.log(valoresTelemetria);

  //crearemos el html
  //usaremos un ciclo para recorrer los Datos

  let html = "";

  for (valor of valoresTelemetria) {
    let row = `

<tr>
 <td>${valor.id}</td>
 <td>${valor.nombreDispositivo}</td>
 <td>${valor.idmensaje}</td>
 <td>${valor.fechaDispositivo}</td>
 <td>${valor.latitud}</td>
 <td>${valor.longitud}</td>
 <td>${valor.temperatura}</td>
 <td>${valor.voltajeBateria}</td>
 <td>${valor.idevento}</td>
 <td>${valor.ciclando}</td>
 <td>${valor.vac}</td>
 <td>${valor.iac}</td>
 <td>${valor.vdc}</td>
 <td>${valor.idc}</td>
 <td>${valor.releciclado}</td>
 <td>${valor.releauxiliar}</td>
 <td>${valor.horometrovac}</td>
 <td>${valor.horometrovdc}</td>
 <td>${valor.fechagrabacion}</td>
 <td>${valor.descripcionevento}</td>
</tr>

`;
    html = html + row;
  }

  document.querySelector("#table-id > tbody").outerHTML = html;
}
