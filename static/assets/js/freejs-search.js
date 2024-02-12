$(document).ready(function () {

  const HOST = '54.237.68.51';


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

        $('.tenders h2').empty();
        $('.tenders .table > tbody').empty();
        $('.tenders .table > tbody').append(data.map(tender => {
          return `<tr>
                       
                        <td><a href="#" class="text-primary">${tender.name}</a></td>
                        <td>${tender.doc_price}</td>
                        <td>${tender.bidbond}</td>
                        <td>${tender.regions}</td>
                        <td>${tender.categories}</td>
                        <td>${tender.ann_date}</td>
                        <td>${tender.closing_date}</td>
                        <td>${tender.isactive}</td>
                        
                        </tr>`

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
