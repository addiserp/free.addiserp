$(document).ready(function () {

  const HOST = '0.0.0.0';


var getcheckedvalue = function (groupname) {
  const datas = {};
  var result = $('input[name="' + groupname + '"]:checked');
  if (result.length > 0) {
  result.each(function () {
    datas[$(this).attr('data-id')] = $(this).attr('data-name');
  });
  return datas;
}
};
 
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
  $('.sidebar-nav #mysearch').click(function () {
    categories = getcheckedvalue('category');
    regions = getcheckedvalue('region');
    languages = getcheckedvalue('language');
    const filters = {
      'categories': categories,
      'regions': regions,
      'languages': languages
    };
    search(filters);
  });
 
  // Display all places when the website is launched
  search();
});
