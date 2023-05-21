function mensaje () {
    alert('Bienvenido')
    console.log('Consola');
}

function eliminar(id) {
    Swal.fire({
        title: 'Confirmar',
        text: 'Esta seguro de desea eliminar este producto?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire('Eliminado!','Producto Eliminado Correctamente','success').then(function() {
              window.location.href = "/delete/"+id+"/";
          })
        }
    })
}

function guardar(id) {
  Swal.fire({
    title: 'title',
    text: 'text',
    icon: 'success',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'success'
  }).then((result) => {
    if (result.isConfirmed) {
      //success
    }
  })
}