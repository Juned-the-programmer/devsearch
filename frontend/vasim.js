let URL = 'http://13.127.139.83:5050/api/v1/create/ics'

let getpetdetail = () => {
    let formdata = {
        "title": "Dinner",
        "description": "it's dinner time",
        "organizerName": "vasim",
        "organizerEmail": "vasim@gmail.com",
        "startDate": "2022-02-23T10:23:31.490Z",
        "daily": true,
        "weekly": false,
        "weekDays": ["MO","WE"],
        "monthly": false,
        "dayOfMonth": 12,
        "petName": "Jojo",
        "routineName": "Playing football",
        "endDate": "2023-02-23T10:23:31.490Z"
    }
    fetch(URL , {method : 'POST' , headers: {'Content-Type': 'application/json'} , body : JSON.stringify(formdata)}).then(
        response => response.json()
    ).then(data => {
        console.log(data)
    })
}

getpetdetail()