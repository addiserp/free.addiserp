$(document).ready(function () {

  const HOST = '54.237.68.51';

  // Get api status
  $.get(`http://${HOST}:5002/api/v1/status/`, data => {
    if (data.status == "OK") {
      $('DIV#api_status').addClass("available");
    } else {
      $('DIV#api_status').removeClass("available");
      $('DIV#api_status').addClass("notavailable");
    }
  });

   // load regions,categories and langua on load
  function loadall () {
    $.ajax({
      type: 'GET',
      url: `http://${HOST}:5002/api/v1/languages`,
      data: JSON.stringify(),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
      $('.sidebar-nav #language-nav').empty();
      $('.sidebar-nav #language-nav').append(data.map(data_language => {
          return `
          <li>
          <input type="checkbox" data-id="${data_language.id}" name="language" data-name="${data_language.name}" style="margin-right: 10px;">${data_language.name}
        </li>
          `
        }));
      }
    });
      // end of load languages
    $.ajax({
      type: 'GET',
      url: `http://${HOST}:5002/api/v1/regions`,
      data: JSON.stringify(),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
      $('.sidebar-nav #region-nav').empty();
 
      $('.sidebar-nav #region-nav').append(data.map(data_region => {
          return `
          <li>
          <input type="checkbox" data-id="${data_region.id}" name="region" data-name="${data_region.name}" style="margin-right: 10px;">${data_region.name}
        </li>
          `
        }));
      }
    });
    $.ajax({
      type: 'GET',
      url: `http://${HOST}:5002/api/v1/categories`,
      data: JSON.stringify(),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
      $('.sidebar-nav #catagory-nav').empty();
 
      $('.sidebar-nav #catagory-nav').append(data.map(data_catagory => {
          return `
          <li>
          <input type="checkbox" data-id="${data_catagory.id}" name ="category" data-name="${data_catagory.name}" style="margin-right: 10px;">${data_catagory.name}
        </li>
          `
        }));
      }
    });
  };
  
  // end load regions


  
  loadall(); 

});
