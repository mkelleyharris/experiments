// Global varioable and functions.

//if (typeof examples == 'undefined') { var examples = {}; }
//if (typeof examples.globals == 'undefined') { examples.globals = {}; }
if (typeof sc_globals == 'undefined') { sc_globals = {}; }

var cpDate = "2017";

//examples.globals.copyrightDate = function(opt_data, opt_ignored) {
sc_globals.getCopyrightDate = function(opt_data, opt_ignored) {
	  return cpDate;
}
	
sc_globals.getCopyrightDateHTML = function(opt_data, opt_ignored) {
	  //return "<p>" + ' 'cpDate;
	  //return "<p align=\"center\">\&\#169 " + "2004 - " + sc_globals.getCopyrightDate() + ' ' + "SourceCell" + '\u2122' + "</p>";
	  return "Copyright " + "\&\#169 " + "2004 - " + sc_globals.getCopyrightDate() + ' ' + "SourceCell" + '\u2122';
}

sc_globals.getSourceCellLogoForWhiteBackgroundHTML = function(opt_data, opt_ignored) {
     return '<a href="index.html"><img alt="" src="images/logo_SourceCell_OpaqueWhite_3Stacks.png" alt="SourceCell" height="30" width="222"></a>';
}



sc_globals.getSourceCellLogoForBlackBackgroundHTML = function(opt_data, opt_ignored) {
     return '<a class="navbar-brand" href="index.html"><img alt="SourceCell" src="images/logo_SourceCell_TransparentBlackCap_3Stacks.png" alt="SourceCell" height="35" width="210"></a>';
}
