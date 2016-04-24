$(document).ready(function () {

  function resetFormElement(e) {
    e.wrap('<form>').closest('form').get(0).reset();
    e.unwrap();
  }

  $('#uploadform').ajaxForm({
    beforeSubmit: function () {
      // Validate input
      $('.has-error').removeClass('has-error');
      var errors = 0;
      $.each(['thefile', 'composer', 'piece'], function (index, name) {
        var elem = $('#' + name);
        if (!(elem.val() && elem.val().length)) {
          elem.parent().addClass('has-error');
          errors++;
        }
      });
      if (errors) {
        return false;
      }
      $('#vidsubmit').addClass('active');
      return true;
    },
    success: function (response) {
      $('#flist').append($('<li><a href="/video/' + response.fname + '.mp4">' + response.fname + '</a></li>'));
      resetFormElement($('#thefile'));
      $('#vidsubmit').removeClass('active');
      $('#thefile').focus();
    }
  })
});
