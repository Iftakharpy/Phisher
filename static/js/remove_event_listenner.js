function removeEventListenners(element){
  let clone = element.cloneNode(true)
  element.parentNode.replaceChild(clone, element);
}

