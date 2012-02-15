(function ($) {
	$(function(){
		// the theme depends on whether we're using grappelli or not
		var theme = !!grappelli ? 'grappelli' : 'standard';
		// for every element that has the attribute data-token-autocomplete, run the tokenfield script
		$("[data-token-autocomplete]").each(function(){
			var $this = $(this),
				// separate the current tags into an array
				current_data_array = $this.val().split(','),
				// create an empty array to store tokens in
				current_data = [],
				// grab the url for pulling tags from
				url = $this.attr('data-token-autocomplete');
			// Parse the current field value into tokens
			for (i = 0; i < current_data_array.length; i++){
				var id = current_data_array[i],
					name = current_data_array[i].replace(/[ ]?"?([^"]*)"?/g,"$1"); // strip spaces and quotes for display
				if (current_data_array[i] !== "") current_data[i] = {'id': id, 'name': name}
			}
			// Initialize the TokenInput
			$this.tokenInput(url, {
				theme: theme,
				prePopulate: current_data,
				preventDuplicates: true,
				onResult: function (results) {
					// When the results have loaded, if the entered phrase is not exactly in the results, add it as a new tag.
					var tag_in_results = false,
						entry_field = $('#token-input-'+$this[0].id),
						new_tag = {
							id: entry_field.val(),
							name: entry_field.val() + " (new tag)"
						};
					for (i = 0; i < results.length; i++) {
						if (results[i]['id'] === '"'+entry_field.val()+'"') tag_in_results = true;
					}
					if (!tag_in_results) results.push(new_tag);
					return results
				}
			});
		})
	});
}).call(this, django.jQuery)