# encoding: utf-8

import factory

from ckanext.accesscontrol import model as extmodel
from ckan.tests import helpers, factories as ckan_factories


class Role(factory.Factory):
    FACTORY_FOR = extmodel.Role

    name = factory.Sequence(lambda n: 'test_role_{0:02d}'.format(n))
    title = factory.LazyAttribute(lambda obj: obj.name.replace('_', ' ').title())
    description = 'A test description for this test role.'

    @classmethod
    def _build(cls, target_class, *args, **kwargs):
        raise NotImplementedError(".build() isn't supported in CKAN")

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        if args:
            assert False, "Positional args aren't supported, use keyword args."

        context = {'user': ckan_factories._get_action_user_name(kwargs)}

        return helpers.call_action('role_create', context=context, **kwargs)


class Permission(factory.Factory):
    FACTORY_FOR = extmodel.Permission

    content_type = factory.Sequence(lambda n: 'a_thing_{0:02d}'.format(n))
    operation = 'an_operation'

    @classmethod
    def _build(cls, target_class, *args, **kwargs):
        raise NotImplementedError(".build() isn't supported in CKAN")

    @classmethod
    def _create(cls, target_class, *args, **kwargs):
        if args:
            assert False, "Positional args aren't supported, use keyword args."

        context = {'user': ckan_factories._get_action_user_name(kwargs)}

        return helpers.call_action('permission_create', context=context, **kwargs)