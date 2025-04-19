$(document).ready(function () {
    console.log("✅ jQuery-версия загружена!");

    function resetSelect($select) {
        $select.html('<option value="">---------</option>');
        $select.prop('disabled', true);
    }

    function enableSelect($select) {
        $select.prop('disabled', false);
    }

    const $typeSelect = $('#id_type');
    const $categorySelect = $('#id_category');
    const $subcategorySelect = $('#id_subcategory');

    resetSelect($categorySelect);
    resetSelect($subcategorySelect);

    $typeSelect.on('change', function () {
        const typeId = $(this).val();
        console.log("📦 Выбран тип:", typeId);

        resetSelect($categorySelect);
        resetSelect($subcategorySelect);

        if (typeId) {
            $.ajax({
                url: '/ajax/load-categories/',
                data: {
                    type: typeId
                },
                success: function (data) {
                    $.each(data, function (index, item) {
                        $categorySelect.append($('<option>', {
                            value: item.id,
                            text: item.name
                        }));
                    });
                    enableSelect($categorySelect);
                }
            });
        }
    });

    $categorySelect.on('change', function () {
        const categoryId = $(this).val();
        console.log("📁 Выбрана категория:", categoryId);

        resetSelect($subcategorySelect);

        if (categoryId) {
            $.ajax({
                url: '/ajax/load-subcategories/',
                data: {
                    category: categoryId
                },
                success: function (data) {
                    $.each(data, function (index, item) {
                        $subcategorySelect.append($('<option>', {
                            value: item.id,
                            text: item.name
                        }));
                    });
                    enableSelect($subcategorySelect);
                }
            });
        }
    });

    if ($typeSelect.val()) {
        $typeSelect.trigger('change');
    }
});
