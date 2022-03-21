function setCookie(cookieName, cookieValue, exdays) {
    let duration = new Date();
    duration.setTime(duration.getTime() + (exdays*24*60*60*1000));
    let expires = "expires="+duration.toUTCString();

    // solves the problem of forbidden characters
    if ('btoa' in window) {
        cookieValue = btoa(cookieValue);
    }

    document.cookie = cookieName + "=" + cookieValue + "; " + expires+';path=/store/cart';
}

function saveCart(inCartItemsNum, cartArticles) {
    setCookie('inCartItemsNum', inCartItemsNum, 5);
    setCookie('cartArticles', JSON.stringify(cartArticles), 5);
}
