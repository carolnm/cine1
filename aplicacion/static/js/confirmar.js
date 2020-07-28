function confirmarEliminacion(id){
    Swal.fire({
        title: '¿ Estas seguro que deseas eliminar la pelicula?',
        text: "No podras deshacer esta acción!!!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar de todos modos!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if(result.value){
            window.location.href = "/eliminar_pelicula/"+id+"/";
        }
      })
}