
var socket = io.connect('http://' + document.domain + ':' + location.port);
// tratamento dos dados a sereme enviados para o server
    function send_info()
    {
          let user_name = $( 'input.username' ).val()
          let user_input = $( 'input.form-control' ).val()
          socket.emit( 'my event', {
            user_name : user_name,
            message : user_input
          } )
          $( 'input.form-control' ).val( '' ).focus();
    }
[]
window.onload = function() {


   socket.on( 'connect', function() {
        socket.emit( 'my event', {
          data: 'User Connected'
        } )

      } )

      socket.on( 'my response', function( msg ) {

        if( typeof msg.user_name !== 'undefined' ) {
          //$( 'h3' ).remove()
          //$( 'div.message_holder' ).append( '<div><b style="color: #000">'+msg.user_name+'</b> '+msg.message+'</div>' )
          var html_code = '<div class="row form-group"> <div class="col col-md-1"><label for="hf-email" class=" form-control-label">'+msg.user_name+'</label></div> <div class="col col-md"><label for="hf-email" class=" form-control-label">'+msg.message+'</label></div> </div>';

          $('#chat-board').append(html_code);
        }
      })

}
