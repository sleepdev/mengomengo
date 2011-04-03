function login()
{
  if( typeof FB == 'undefined' )
    document.location = "/login";
  else
    FB.login(function(response) {
      if (response.session)
        document.location = "/";
    });
}
function logout()
{
  FB.logout(function(response) {
    document.location = "/";
  })
}

$('.toggle').click( function(){ 
  if( $(this).hasClass('clicked') ) {
    $(this).removeClass('clicked');
  } else {
    $(this).addClass('clicked');
  }
})
