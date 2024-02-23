$(document).ready(function () {

  const HOST = '0.0.0.0';
//  const HOST = '54.227.128.161';

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
        $('.tenders h2').append("Search Result for:")
        $('.tenders .table > tbody').empty();
        $('.tenders .table > tbody').append(data.map(tender => {
          return `<tr>
                       
                        <td><a href="#" class="text-primary">${tender.name}</a></br>
                        Document Price:-${tender.doc_price} Bidbond Amount :-${tender.bidbond} </br>
                        Date Of Announcment :-${tender.ann_date} closing Date :- ${tender.closing_date}
                        Is Active :- ${tender.isactive}</td>
                        
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
