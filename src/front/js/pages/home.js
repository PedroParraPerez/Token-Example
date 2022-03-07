import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);
// Con este Fetch lo que estamos creando gracias a la ruta que guardamos en country db.session.commit guardaremos el pais Prueba
  

useEffect(()=>{
  CreateCountry() //Creamos un pais en la base de datos cada vez que refrescamos la pagina con el name de name: pero solo podemos poner un mismo pais una vez por que el valor no se puede repetir (Si se repite en la relacion, pero no en el listado, es decir, españa tiene muchas ciudades pero no existen dos españas)
}, [])

let asd = "hola"
const CreateCountry = () => {
  fetch(
    "https://3001-pedroparraperez-tokenexa-1gdv6yaxh6q.ws-eu34xl.gitpod.io/api/countries/create",
    {
      method: "POST",
      body: JSON.stringify({
        name: asd,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }
  ).then((response) => console.log(response));

}



  return (
    <div className="text-center mt-5">
      <h1>Hello Rigo!!</h1>
      <p>
        <img src={rigoImageUrl} />
      </p>
      <div className="alert alert-info">
        {store.message ||
          "Loading message from the backend (make sure your python backend is running)..."}
      </div>
      <p>
        This boilerplate comes with lots of documentation:{" "}
        <a href="https://github.com/4GeeksAcademy/react-flask-hello/tree/95e0540bd1422249c3004f149825285118594325/docs">
          Read documentation
        </a>
      </p>
    </div>
  );
};
