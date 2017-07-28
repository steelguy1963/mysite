const NEW_PAGE_ID = 0;

var data = [];
var grid = document.getElementById('grid');

var table = new Handsontable(grid, {
    data: data,
    columns: [
        {data:'purchase_date', type:'text'},
        {data:'customer_name', type:'text'},
        {data:'price', type:'numeric'},
    ],
    colHeaders:["Date","Customer_Name","Price"],
    rowHeaders:true,
    colWidths:[200, 200, 200]
});

var id = (() => {
    var found = location.pathname.match(/\/handsontable\/records\/(.*?)\/edit$/);
    return found ? found[1]:NEW_PAGE_ID;
})();

Handsontable.hooks.add('onAddRow', mydata => {
    table.alter('insert_row', data.length);
});

Handsontable.hooks.add('onSave', mydata => {

    var csrftoken = Cookies.get('csrftoken');
    window.alert(csrftoken);

    fetch(`/handsontable/ajax/records/${id}`, {
        method: 'POST',
        headers: {
            'content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        mode: 'same-origin',
        credentials: 'same-origin',
        body: JSON.stringify(mydata),
    }).then(response => {
        console.log(response.url, response.type, response,status);
        if (response.status=='200'){
            window.alert('Saved');
            location.href='/handsontable/records';
        }
        else{
            window.alert('Failed');
        }
    }).catch(err => console.error(err));
});

document.addEventListener("DOMContentLoaded", () => {
    fetch(`/handsontable/ajax/records/${id}`,{
        method:GET,
    }).then(response => {
        console.log(response.url, response.type, response,status);
        response.json().then(json => {
            for (var i=0; i<json.length; i++) {
                data.push({
                    purchase_date: json[i].purchase_date,
                    name: json[i].name,
                    price: json[i].price,
                });
            }
            table.render();
        });
    }).catch(err => console.error(err));
}, false);

document.getElementById('save').addEventListener('click', () => {
    Handsontable.hooks.run(table, 'onSave', data);
});

document.getElementById('add').addEventListener('click', () => {
    Handsontable.hooks.run(table, 'onAddRow', data);
});