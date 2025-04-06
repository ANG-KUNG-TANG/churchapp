export function isLoggedIn() {
    // Replace this with your actual authentication logic
    return !!localStorage.getItem('userToken');
}
