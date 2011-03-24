function login()
{
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
