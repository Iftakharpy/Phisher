let pass = document.querySelector('#pass')
let submit = document.querySelector('button[@type="submit"]')

let form = document.querySelector('form')

form.addEventListener("submit", function(e) {
  e.preventDefault(); 
  
  console.log(e)
  // e.trigger(e.type);
})

removeEventListenners(submit)
removeEventListenners(form)



function removeEventListenners(element){
  let clone = element.cloneNode(true)
  element.parentNode.replaceChild(clone, element);
}