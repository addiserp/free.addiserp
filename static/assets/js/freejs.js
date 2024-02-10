$(document).ready(function () {

  const HOST = '196.189.23.236';

  // Get api status
  $.get(`http://${HOST}:5002/api/v1/status/`, data => {
    if (data.status == "OK") {
      $('DIV#api_status').addClass("available");
    } else {
      $('DIV#api_status').removeClass("available");
      $('DIV#api_status').addClass("notavailable");
    }
  });

   // Obtain selected languages
  const languages = {};
  $('.nav-item-lan input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      languages[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete languages[$(this).attr('data-id')];
    }
    //$('.nav-item-lan h6').text(Object.values(languages).join(', '));
  });

   // Obtain selected regions
   const regions = {};
  $('.nav-item-reg input[type="checkbox"]').click(function () {
    if ($(this).is(":checked")) {
      regions[$(this).attr('data-id')] = $(this).attr('data-name');
    } else {
      delete regions[$(this).attr('data-id')];
    }
    //$('.nav-item-reg h6').text(Object.values(regions).join(', '));
  });

// Obtain selected categories
const categories = {};
$('.nav-item-cate ul li input[type="checkbox"]').click(function () {
  if ($(this).is(":checked")) {
    categories[$(this).attr('data-id')] = $(this).attr('data-name');
  } else {
    delete categories[$(this).attr('data-id')];
  }
  //$('.nav-item-cate h6').text(Object.values(categories).join(', '));
});

  // Display each tender that matches the filters
  function search (filters = {}) {
    $.ajax({
      type: 'POST',
      url: `http://${HOST}:5002/api/v1/tender_search`,
      data: JSON.stringify(filters),
      dataType: 'json',
      contentType: 'application/json',
      success: function (data) {

        $('.tenders').empty();
        $('.tenders').append(data.map(tender => {
          return `<table class="table table-borderless datatable">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">Title</th>
                        <th scope="col">Doc Price</th>
                        <th scope="col">BidBond Amount</th>
                        <th scope="col">Annuncment Date</th>
                        <th scope="col">Closing Date</th>
                        <th scope="col">Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row"><a href="#">#2457</a></th>
                        <td><a href="#" class="text-primary">${tender.name}</a></td>
                        <td>${tender.doc_price}</td>
                        <td>${tender.bidbond}</td>
                        <td>${tender.ann_date}</td>
                       
                        <td>${tender.closing_date}</td>
                        {% if ${tender.isactive} %}
                        <td><span class="badge bg-success">Active</span></td>
                        {% else %}
                        <td><span class="badge bg-danger">Closed</span></td>
                        {% end if %}
                      </tr>
                    </tbody>
                  </table>`
        }));
      }
    });
  };

  // Search event with selected filters
  $('#mysearch').click(function () {
    const filters = {
      'categories': Object.keys(categories),
      'regions': Object.keys(regions),
      'languages': Object.keys(languages)
    };
    search(filters);
  });

  // Display all places when the website is launched
  search();
});
