$(document).ready(function () {

  const HOST = 'localhost';

  // Get api status
  $.get(`http://${HOST}:5002/api/v1/status/`, data => {
    if (data.status == "OK") {
      $('DIV#api_status').addClass("available");
    } else {
      $('DIV#api_status').removeClass("available");
      $('DIV#api_status').addClass("notavailable");
    }
  });

 
  // Obtain selected categories
  const htmlcata = {};
  $('.htmlcategories ul li input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      htmlcata[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete htmlcata[$(this).attr('data-id')];
    }
    $('.htmlcategories h6').text(Object.values(htmlcata).join(', '));
  });

   // Obtain selected amenities
  const languages = {};
  $('.language input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      languages[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete languages[$(this).attr('data-id')];
    }
    $('.language h6').text(Object.values(languages).join(', '));
  });

   // Obtain selected regions
   const regions = {};
  $('.region input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      regions[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete regions[$(this).attr('data-id')];
    }
    $('.region h6').text(Object.values(regions).join(', '));
  });

  // Display each place that matches the filters
  function search (filters = {}) {
    $.ajax({
      type: 'POST',
      url: `http://${HOST}:5002/api/v1/tender_search`,
      data: JSON.stringify(filters),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {
        $('SECTION.places').empty();
        $('SECTION.places').append(data.map(place => {
          return `<article>
                    <div class="title_box">
                      <h2>${place.name}</h2>
                      <div class="price_by_night">${place.price_by_night}</div>
                    </div>
                    <div class="information">
                      <div class="max_guest">${place.max_guest} Guests</div>
                      <div class="number_rooms">${place.number_rooms} Bedrooms</div>
                      <div class="number_bathrooms">${place.number_bathrooms} Bathrooms</div>
                    </div>
                    <div class="description">
                      ${place.description}
                    </div>
                  </article>`
        }));
      }
    });
  };

  // Search event with selected filters
  $('#search').click(function () {
    const filters = {
      'htmlcata': Object.keys(cata),
      'regions': Object.keys(regions),
      'languages': Object.keys(languages)
    };
    search(filters);
  });

  // Display all places when the website is launched
  search();
});
