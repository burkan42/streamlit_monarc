var flow_terms = src="Flow1.txt", id="text", type="text";
var suit_terms = src="Suites.txt", id="text", type="text";
 
function autocompletesuit(input) {
  if (input == '') {
    return [];
  }
  var reg = new RegExp(input)
  return suit_terms.filter(term);
}
 
function showsuit(val) {
  res = document.getElementById("resultsuit");
  res.innerHTML = '';
  let list = '';
  let terms = autocompletesuit(val);
  for (i=0; i<terms.length; i++) {
    list += '<li>' + terms[i] + '</li>';
  }
  res.innerHTML = '<ul>' + list + '</ul>';
}

function autocompleteflow1(input) {
    if (input == '') {
      return [];
    }
    var reg = new RegExp(input)
    return flow_terms.filter(term);
}


function showflow1(val) {
    res = document.getElementById("resultflow1");
    res.innerHTML = '';
    let list = '';
    let terms = autocompleteflow1(val);
    for (i=0; i<terms.length; i++) {
      list += '<li>' + terms[i] + '</li>';
    }
    res.innerHTML = '<ul>' + list + '</ul>';
}


function autocompleteflow2(input) {
    if (input == '') {
      return [];
    }
    var reg = new RegExp(input)
    return flow_terms.filter(term);
}
   
function showflow2(val) {
    res = document.getElementById("resultflow2");
    res.innerHTML = '';
    let list = '';
    let terms = autocompleteflow2(val);
    for (i=0; i<terms.length; i++) {
      list += '<li>' + terms[i] + '</li>';
    }
    res.innerHTML = '<ul>' + list + '</ul>';
}

function filter(term) {
    if (term.match(reg)) {
      return term;
    }
};