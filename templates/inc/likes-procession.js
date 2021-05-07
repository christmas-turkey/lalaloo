const csrf = document.createElement('div')
csrf.innerHTML = '{% csrf_token %}'

const xhr = new XMLHttpRequest()


function sendLike(caller) {
  
  // Retrieving metadata from like's or dislike's link
  const adress = caller.dataset.adress
  const uuid = caller.dataset.videoUuid
  const type = caller.dataset.likeType

  xhr.open('POST', adress, true);

  let likesQuantity = null;

  if (type === "like") {
    likesQuantity = caller.querySelector('#likes')

  } else if (type === "dislike") {
    likesQuantity = caller.querySelector('#dislikes')

  }


  xhr.setRequestHeader('X-CSRFToken', csrf.firstChild.value)


  let likeValue = null;

  // Check whether user already liked the video
  if (localStorage.getItem([`${uuid}__${type}`])) {

    likeValue = -1

    likesQuantity.innerHTML = +likesQuantity.innerHTML + likeValue

    localStorage.removeItem(`${uuid}__${type}`)
    xhr.send(JSON.stringify({like: likeValue, like_type: type}))

  } else {

    likeValue = 1

    likesQuantity.innerHTML = +likesQuantity.innerHTML + likeValue
    
    localStorage.setItem(`${uuid}__${type}`, true)
    xhr.send(JSON.stringify({like: likeValue, like_type: type}))
  
  }

  caller.classList.toggle('liked')
    
}


(function checkLikedLinks(links) {

  for (let link of links) {

    const uuid = link.dataset.videoUuid
    const type = link.dataset.likeType

    if (localStorage.getItem([`${uuid}__${type}`])) {

      link.classList.add('liked')
    
    }

  }

})(document.getElementsByClassName('like-link'))
