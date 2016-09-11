"""
todo
"""

import dploy.utils as utils


class AbstractBaseAction():
    # pylint: disable=too-few-public-methods
    """
    todo
    """
    def __init__(self):
        pass

    def _logic(self):
        pass

    def execute(self):
        """
        todo
        """
        self._logic()


class SymbolicLink(AbstractBaseAction):
    # pylint: disable=too-few-public-methods
    """
    todo
    """
    def __init__(self, subcmd, source, dest):
        super().__init__()
        self._source = source
        self._source_relative = utils.get_relative_path(source, dest.parent)
        self.subcmd = subcmd
        self._dest = dest

    @property
    def dest(self):
        """
        todo
        """
        return self._dest

    @property
    def source(self):
        """
        todo
        """
        return self._source

    @property
    def source_relative(self):
        """
        todo
        """
        return self._source_relative

    def _logic(self):
        self.dest.symlink_to(self.source_relative)

    def __repr__(self):
        return "dploy {subcmd}: link {dest} => {source}".format(
            subcmd=self.subcmd, dest=self.dest, source=self.source)


class AlreadyLinked(AbstractBaseAction):
    # pylint: disable=too-few-public-methods
    """
    todo
    """
    def __init__(self, subcmd, source, dest):
        super().__init__()
        self.source = source
        self.dest = dest
        self.subcmd = subcmd

    def _logic(self):
        pass

    def __repr__(self):
        return "dploy {subcmd}: already linked {dest} => {source}".format(
            subcmd=self.subcmd,
            source=self.source,
            dest=self.dest)


class AlreadyUnlinked(AbstractBaseAction):
    # pylint: disable=too-few-public-methods
    """
    todo
    """
    def __init__(self, subcmd, source, dest):
        super().__init__()
        self.source = source
        self.dest = dest
        self.subcmd = subcmd

    def _logic(self):
        pass

    def __repr__(self):
        return "dploy {subcmd}: already unlinked {dest} => {source}".format(
            subcmd=self.subcmd,
            source=self.source,
            dest=self.dest)


class UnLink(AbstractBaseAction):
    # pylint: disable=too-few-public-methods
    """
    todo
    """
    def __init__(self, subcmd, target):
        super().__init__()
        self.target = target
        self.subcmd = subcmd

    def _logic(self):
        self.target.unlink()

    def __repr__(self):
        return "dploy {subcmd}: unlink {target} => {source}".format(
            subcmd=self.subcmd,
            target=self.target,
            source=self.target.resolve())

class MakeDirectory(AbstractBaseAction):
    # pylint: disable=too-few-public-methods
    """
    todo
    """
    def __init__(self, subcmd, target):
        super().__init__()
        self.target = target
        self.subcmd = subcmd

    def _logic(self):
        self.target.mkdir()

    def __repr__(self):
        return "dploy {subcmd}: make directory {target}".format(
            target=self.target,
            subcmd=self.subcmd)

class RemoveDirectory(AbstractBaseAction):
    # pylint: disable=too-few-public-methods
    """
    Action to remove a directory
    """
    def __init__(self, subcmd, target):
        super().__init__()
        self.target = target
        self.subcmd = subcmd

    def _logic(self):
        utils.rmtree(self.target)

    def __repr__(self):
        msg = "dploy {subcmd}: remove directory {target}"
        return msg.format(target=self.target, subcmd=self.subcmd)
