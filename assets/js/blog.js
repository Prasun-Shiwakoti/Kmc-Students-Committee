function copyLink(id){
    url = `${window.location.origin}/blogs.html/${id}`;
    var textarea = document.createElement("textarea");
    textarea.textContent = url;
    textarea.style.position = "fixed";  // Prevent scrolling to bottom of page in Microsoft Edge.
    document.body.appendChild(textarea);
    textarea.select();
    textarea.setSelectionRange(0, 99999);
    document.execCommand("copy");
    // navigator.clipboard.writeText(url);
    alert("Link Copied!!!");
    document.body.removeChild(textarea);
}