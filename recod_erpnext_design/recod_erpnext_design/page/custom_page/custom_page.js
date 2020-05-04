frappe.pages['custom_page'].on_page_load = function(wrapper) {
	let page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Custom Page',
		single_column: true
	});
};
