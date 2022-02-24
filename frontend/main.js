let projectsUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects = () => {
    fetch(projectsUrl).then(
            response => response.json()
        ).then( data => {
                console.log(data)
                buildProjects(data)
            }
        )
}

let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById("projects--wrapper")

    projectsWrapper.innerHTML = ''

    for(let i=0; projects.length > i; i++){
        let project = projects[i]
        
        let projectcard = `
            <div class="project--card">
                <img src="http://127.0.0.1:8000${project.featured_image}"></img>
                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                    </div>
                    <i>${project.vote_ratio}% Postitivr Feedback</i>
                    <p>${project.description.substring(0,150)}</p>
                </div>
            </div>
        `
        projectsWrapper.innerHTML += projectcard
    }

    addVoteEvents()
}

let addVoteEvents = () => {
    let voteBtn = document.getElementsByClassName('vote--option')

    let token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1Njg2MDE0LCJpYXQiOjE2NDU2ODU0MTQsImp0aSI6IjljZjVkMTA4NGZlZTQ3NDg5N2I1YzZlYWRlNzQwNWYxIiwidXNlcl9pZCI6MTN9.gInLC9KmgIBnmsvoNybe2Mm_JCvVSybBD1wQ7WlaWN4'

    for(let i=0;voteBtn.length > i;i++){
        voteBtn[i].addEventListener('click' , (e) => {
            let  vote = e.target.dataset.vote
            let project = e.target.dataset.project
            
            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/` , {
                method : 'POST' , headers : {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body : JSON.stringify({
                    "value" : vote
                })
            })
            .then(response => response.json())
            .then(data => {
                console.log(data)
                getProjects()
            })
        })
    }
}

getProjects()  
