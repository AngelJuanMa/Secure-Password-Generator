
function toHash(form) {
    var passHashed = sha256(document.getElementById('pass').value)
    var publicHashed = sha256(document.getElementById('public').value)
    var dateHashed = sha256(document.getElementById('date').value)
    var hash = sha256(dateHashed + passHashed + publicHashed);
    hash = hash.substring(0, 20)
    var password = "$#" + hash.replace("a", "A").replace("b", "B").replace("f", "F") + "%!"

    navigator.clipboard.writeText(password);
}
