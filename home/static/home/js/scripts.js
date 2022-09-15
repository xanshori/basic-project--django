//get search form and page
let searchform = document.getElementById('searchForm')
let pagelinks= document.getElementsByClassName('page-link')
let i = 0
//ensuree search form exist

if(searchform){
    for(i; pagelinks.length >i; i++){
        pagelinks[i].addEventListener('click',function(e){
            e.preventDefault()
            //get the data attribut.

            let page = this.dataset.page
            //add hiden searchinput to form
            searchform.innerHTML +=`<input value=${page} name="page" hidden/>`


            //submit form
            searchform.submit()
        })
        
    }
}