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
            a.setAttribute( 'href', `/page/${ p.title }` );
            a.setAttribute( 'class', 'text-decoration-none' );
            a.setAttribute( 'id', `anchor-${ p.title }` );
            div.setAttribute( 'id', `div-${ p.title }`);

            h1.innerText = p.title;
            h1.append( img );
            pa.innerText = p.description;
            div.append( h1, pa );
            a.append( div );
            container.append( a );
        }
    }
    
    const searchPages = async( term, limit = 25 ) => {
        const url = `${ searchPagesEndpoint }q=${ term }&limit=${ limit }`;
        const promise = await axios.get( url );
        const pages = promise.data.pages;
        clearPages();
        appendPages( pages );
    }

    const clearPages = () => {
        searchPagesContainer.innerHTML = '';
        return searchPagesContainer;
    }

});

