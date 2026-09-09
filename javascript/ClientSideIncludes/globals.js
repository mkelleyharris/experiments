// Global varioable and functions.

if (typeof examples == 'undefined') { var examples = {}; }
if (typeof examples.globals == 'undefined') { examples.globals = {}; }

var cpDate = "2017";

examples.globals.copyrightDate = function(opt_data, opt_ignored) {
	  return cpDate;
};

