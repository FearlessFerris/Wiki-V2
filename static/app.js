/* 
    Wikipedia Endpoints

*/

const searchPagesEndpoint = 'https://en.wikipedia.org/w/rest.php/v1/search/page?';
const getPageEndpoint = 'https://en.wikipedia.org/w/rest.php/v1/page/';

document.addEventListener( 'DOMContentLoaded', function(){
    
    // Logic for page searches 
    const searchPageInput = document.getElementById( 'search-page-term' );
    const searchPagesContainer = document.getElementById( 'search-pages-container' );
    
    if ( searchPageInput ){
        searchPageInput.addEventListener( 'input', debounce(function(){
            let term = searchPageInput.value;
            if( term === '' ){
                clearPages();
            }
            else{
                searchPages( term );
            }
        }, 250 ))
    }

    function debounce( func, delay ){
        let timer;
        return function(){
            clearTimeout( timer );
            timer = setTimeout(() => {
                func.apply( this.arguments );
            }, delay );
        };
    }

    const appendPages = ( pages ) => {
        for( let p of pages ){
            const container = document.getElementById( 'search-pages-container' );
            const div = document.createElement( 'div' );
            const pa = document.createElement( 'p' );
            const h1 = document.createElement( 'h1' );
            const a = document.createElement( 'a' );
            const img = document.createElement( 'img' );

            if( p.thumbnail && p.thumbnail.url ){
                img.setAttribute( 'src', p.thumbnail.url );
                img.setAttribute( 'class', 'rounded 100px mx-3')
            }

            h1.setAttribute( 'class', 'text-info' );
            pa.setAttribute( 'class', 'text-info text-decoration-none' );
            console.log( p.title );
            a.setAttribute( 'href', `/page/${ p.title }` );
            console.log( a );
            a.setAttribute( 'class', 'text-decoration-none' );

            h1.innerText = p.title;
            h1.append( img );
            pa.innerText = p.description;
            div.append( h1, pa );
            a.append( div );
            container.append( a );

            a.addEventListener( 'click', function() {
                // e.preventDefault();
                getPageInfo( p.title );
            });
        }
    }
    
    const searchPages = async( term, limit = 25 ) => {
        const url = `${ searchPagesEndpoint }q=${ term }&limit=${ limit }`;
        const promise = await axios.get( url );
        const pages = promise.data.pages;
        clearPages();
        appendPages( pages );
        console.log( url );
        console.log( pages );
    }

    const clearPages = () => {
        searchPagesContainer.innerHTML = '';
        return searchPagesContainer;
    }

    const base = document.getElementsByTagName( 'base' )
    for ( let i of base ) {
        i.setAttribute('href', 'http://127.0.0.1:5000/')
    }
    
    // // Logic for page information 
    // const getPageInfo = async ( title ) => {
    //     const url = `${ getPageEndpoint }${ title }/html`;
    //     const promise = await axios.get( url );
    //     const html = promise.text;
    //     console.log( promise );
    //     console.log( html );

    //     appendPageInfo( html );

    // }

    // const appendPageInfo = ( res ) => {
    //     const container = document.getElementById( 'page-html' );
    //     console.log( container );
    //     console.log( res.data );
    //     container.append( res.data );
    // }
    
});

