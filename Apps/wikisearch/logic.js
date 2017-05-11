searchWikipedia = function(word){
var query = word.selectionText;
chrome.tabs.create({url: "https://en.wikipedia.org/wiki/" + query});
};
 

chrome.contextMenus.create({
"title": "Wiki Search",
"contexts":["selection"],
"onclick": searchWikipedia
});