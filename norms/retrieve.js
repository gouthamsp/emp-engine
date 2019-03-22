var history = require('observ-history')

history(function (path) {
  //=> (popstate)
})

history()
//=> current path

history.set(path)
//=> pushState