const csrf = document.createElement('div')
csrf.innerHTML = '{% csrf_token %}'

const xhr = new XMLHttpRequest()


function sendLike(target) {

  const adress = target.dataset.adress
  const uuid = target.dataset.videoUuid
  const type = target.dataset.likeType
  
  // Change link's style after clicking
  target.classList.toggle('liked')

  xhr.open('POST', adress, true);

  let likesQuantity = null;

  if (type === "like") {
    likesQuantity = target.querySelector('#likes')

  } else if (type === "dislike") {
    likesQuantity = target.querySelector('#dislikes')

  }


  xhr.onreadystatechange = () => {

    if (xhr.readyState === 4 && xhr.status === 200) {

      const response = JSON.parse(xhr.responseText);
      likesQuantity.innerHTML = +likesQuantity.innerHTML + response.like
      
      }

    }
  
  xhr.setRequestHeader('X-CSRFToken', csrf.firstChild.value)
  
  // Check whether user already liked the video
  if (localStorage.getItem([`${uuid}__${type}`])) {
    
    localStorage.removeItem(`${uuid}__${type}`)
    xhr.send(JSON.stringify({like: -1, like_type: type}))

  } else {
    
    localStorage.setItem(`${uuid}__${type}`, true)
    xhr.send(JSON.stringify({like: 1, like_type: type}))
  
  }
    
}


(function checkLikedLinks(links) {

  for (let link of links) {

    const adress = link.dataset.adress
    const uuid = link.dataset.videoUuid
    const type = link.dataset.likeType

    if (localStorage.getItem([`${uuid}__${type}`])) {

      link.classList.add('liked')
    
    }

  }

})(document.getElementsByClassName('like-link'))
