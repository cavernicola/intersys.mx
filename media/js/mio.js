$(document).ready(function() {
   // do stuff when DOM is ready
   $("a").click(function() {
     alert("Hello world!");
	 event.preventDefault();
   });
 });
