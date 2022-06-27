# Final-Coderhouse-cinema-blog
BLOG CINEMA
En este blog, los usuarios podrán crear un perfil y así visualizar las reviews de las distintas películas pre-cargadas.
Detallamos paso a seguir para su correcto funcionamiento:

En la página "INICIO" se encontrarán con la siguiente información:

    a. Crear cuenta: Haciendo click en este botón, podrán crear un usuario, registrando username y password. Una vez creado el usuario, tendrán acceso a iniciar sesión.
       Luego de iniciar sesión, haciendo click en el botón "Perfil", se editarán los datos del usuario creado pudiendo adicionar "nombre", "apellido" y "correo electrónico".
    
    b. Todas las reviews: haciendo click sobre el botón, podrán visualizar todas las reviews previamente cargadas, con el detalle del usuario que las cargó y su fecha.
       Haciendo click en el nombre de cada película, ingresarán asu review, donde verán el nombre de la película, su director, fecha de estreno y breve descripción.
       En caso de querer agregar una nueva review, deben clickear el botón "Nueva Review". Allí podrán una nueva película con sus correspondientes datos.
       Además cuentan con los botones "Borrar" y "Editar" para poder borrar o editar la review seleccionada.
    
    c. Buscar Film: para poder buscar un review en particular, haciendo click en el botón "Buscar film", se desplagará un buscador donde colocando una palabra y buscará la película que contenga esa palabra en su título.
       En caso de no encontrar nada, mostrará un mensaje de "Aún no hay reviews".
    
    d. Haciendo click en la palabra "CINEMA" del encabezado, vuelven a la página de Inicio. Haciendo click tanto en el texto "Todas las reviews" como en su botón, podrán acceder al listado de las reviews cargadas.
       Lo mismo sucederá si quieren acceder tanto al texto "About us" como su botón, podrán obtener información sobre las creadores del blog con una breve descripción.
    
    e. Si ya completaron, revisaron y editaron la información que consideraban pertinente, puede proceder con cerrar sesión haciendo click en el botón "Salir de mi cuenta", y de este modo volverán la página de inicio.
       Podrán visualizar todas las reviews pero no editarlas, ya que para ello es necesario contar con un usuario creado.

    e. Por último, desde el usuario administrador (user y pass en comentarios de entrega final - plataforma coderhouse -) se podrán administar las reviews publicadas como así también, los usuarios y agregar imagenes a sus perfiles (avatars). Aquí el link al video demostrativo:
    
    https://drive.google.com/file/d/18hIYKtleNgQJoj231tXJxfGmi8CkfsG_/view?usp=sharing
   

Esperamos que disfruten de nuestro blog y los esperamos con novedades sobre los próximos estrenos!!!

Para poder correr el blog:

```bash
python manage.py migrate
python manage.py runserver
```

Luego ingrese a http://localhost:8000/inicio/

