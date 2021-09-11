
def test_del_group(app):
    if len(app.groups.get_group_list()) == 1:
        app.groups.add_new_group("new group")
    old_list = app.groups.get_group_list()
    group = old_list[1]
    app.groups.del_group()
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)
